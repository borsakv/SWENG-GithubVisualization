from github import Github
import pygal
import json

def main():
    token = input("Welcome to Vitali's GitHub API.\nPlease enter your GitHub token: ")

    try:
        user = input("Please enter a GitHub username: ")
        g = Github(token)
        user = g.get_user(user)
        print(f"\nGitHub Profile: {user.login} (https://github.com/{user.login})")       

        getData(user)
    except:
        print("\nAn Error Ocurred!\nProgram terminated.")

# Gets data from GitHub using the username provided, saves any relevant information into a JSON file and saves information to
#   be used to visualize the data.
def getData(user):
    repositories = {}
    repository_info = {}
    repository_languages = {}

    repository_names = []
    commit_data = []
    language_data = {}

    for repository in user.get_repos():
        commits = 0

        repository_languages = repository.get_languages()

        repository_info["languages"] = dict(repository_languages)
        if repository.get_stats_commit_activity():
            commits = repository.get_commits().totalCount
        else:
            commits = 0
        repository_info["commits"] = commits

        repositories[repository.full_name] = dict(repository_info)

        repository_names.append(repository.full_name)
        commit_data.append(commits)
        for language in repository_info["languages"]:
            if language in language_data:
                language_data[language].append(repository_info["languages"][language])
            else:    
                language_data[language] = [repository_info["languages"][language]]

    visualize(user, repository_names, commit_data, language_data)

    profile = {
        "username": user.login,
        "name": user.name,
        "followers": user.followers,
        "following": user.following,
        "repositories": dict(repositories)
    }

    json_object = json.dumps(profile, indent=4)

    f = open("data.json", "w")
    f.write(json_object)
    
# Generates visuals in the web-browser.
def visualize(user, repo_names, commit_data, language_data):
    # Line chart of commits of the user by repositories.
    commit_chart = pygal.Line(width = 800, height = 800, explicit_size = 800)
    commit_chart.title = "Commits By Repository for " + user.name
    commit_chart.x_labels = map(str, repo_names)
    commit_chart.add("Commits", commit_data)
    commit_chart.render_in_browser()

    # Pie chart of languages used by the user.
    language_chart = pygal.Pie(width = 800, height = 800, explicit_size = 800)
    language_chart.title = "Language Usage for " + user.name
    languages = language_data.keys()
    for language in languages:
        language_chart.add(language, language_data[language])
    language_chart.render_in_browser()

    # Bar chart of the users followers vs their following.
    followers_chart = pygal.Bar(width = 800, height = 800, explicit_size = 800)
    followers_chart.title = "Followers vs Following for " + user.name
    followers_chart.add("Followers", user.followers)
    followers_chart.add("Following", user.following)
    followers_chart.render_in_browser()

if __name__ == "__main__":
    main()