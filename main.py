from src import dushuge

if __name__ == '__main__':
    novel_name = input("Enter the name of the novel: ")
    novel = dushuge.Dushuge(novel_name)
    novel.get_novel_info()