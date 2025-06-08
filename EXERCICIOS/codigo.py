import requests
from bs4 import BeautifulSoup
import os

def get_branch(url):
    """Tenta descobrir o nome do branch principal (main ou master)."""
    response = requests.get(url)
    if "tree/main" in response.text:
        return "main"
    elif "tree/master" in response.text:
        return "master"
    return None

def get_python_files(repo_url, branch):
    """Retorna lista de arquivos .py no repositório."""
    files = []
    repo_path = repo_url.replace("https://github.com/", "")
    tree_url = f"https://github.com/{repo_path}/tree/{branch}"

    def explore_folder(folder_url):
        res = requests.get(folder_url)
        soup = BeautifulSoup(res.text, "html.parser")
        for link in soup.find_all("a", class_="js-navigation-open Link--primary"):
            href = link.get("href")
            if href.endswith(".py"):
                files.append(href)
            elif "/tree/" in href:
                explore_folder("https://github.com" + href)

    explore_folder(tree_url)
    return files

def fetch_py_snippet(raw_url):
    """Pega as primeiras 5 linhas do arquivo."""
    try:
        res = requests.get(raw_url)
        if res.status_code == 200:
            lines = res.text.splitlines()
            return "\n".join(lines[:5]) + "\n\n"
    except:
        pass
    return ""

def main():
    with open("repos.txt", "r") as file:
        repos = [line.strip() for line in file if line.strip()]

    with open("coletado.py", "w", encoding="utf-8") as output:
        for repo in repos:
            print(f"🔍 Processando: {repo}")
            branch = get_branch(repo)
            if not branch:
                print(f"❌ Branch não encontrado para {repo}")
                continue

            py_files = get_python_files(repo, branch)
            for file_path in py_files:
                raw_url = file_path.replace("/blob/", "/").replace(
                    "github.com", "raw.githubusercontent.com")
                snippet = fetch_py_snippet("https://" + raw_url)
                if snippet:
                    output.write(f"# Arquivo: {file_path}\n")
                    output.write(snippet)

    print("✅ Coleta finalizada! Código salvo em 'coletado.py'.")

if __name__ == "__main__":
    main()
# Codigo python GPT