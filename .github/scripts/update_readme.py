import os
import urllib.parse

def get_project_folders():
    """
    Get a list of project folders in the current directory.
    """
    folders = [f.name for f in os.scandir('.') if f.is_dir() and not f.name.startswith('.') and f.name != '-p']
    # Exclude .github folder
    if ".github" in folders:
        folders.remove(".github")
    folders.sort()
    return folders

def get_project_description(folder):
    """
    Get the description of a project from its README file.
    """
    readme_path = os.path.join(folder, 'README.MD')
    if not os.path.exists(readme_path):
        readme_path = os.path.join(folder, 'readme.md')

    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            for line in f:
                if len(line.strip()) > 0 and not line.strip().startswith("#"):
                    return line.strip()
    return "No description available."

def update_readme(projects):
    """
    Update the main README.md file with the list of projects.
    """
    readme_path = 'README.MD'
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    project_list_md = "\n".join([f"- [{project}](./{urllib.parse.quote(project)}/) - {get_project_description(project)}" for project in projects])

    # Use a placeholder in the README to mark where the project list should go.
    start_placeholder = "<!-- PROJECTS_LIST_START -->"
    end_placeholder = "<!-- PROJECTS_LIST_END -->"

    start_index = content.find(start_placeholder)
    end_index = content.find(end_placeholder)

    if start_index != -1 and end_index != -1:
        new_content = (
            content[:start_index + len(start_placeholder)] +
            "\n" +
            project_list_md +
            "\n" +
            content[end_index:]
        )
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("README.MD updated successfully.")
    else:
        print("Placeholders not found in README.MD. Could not update.")

if __name__ == "__main__":
    project_folders = get_project_folders()
    update_readme(project_folders)
