def get_cats_info(path):
    try:
        with open(path,'r') as file:
            cats=[]
            for line in file.readlines():
                id,name,age=line.strip().split(',')
                cats.append({'id':id, 'name':name,'age':age})
            return cats
    except FileNotFoundError:
        return('file not found')
    except IOError or OSError:
        return('cant open file')
    
def main():
    print(get_cats_info('cats.txt'))

if __name__=="__main__":
    main()