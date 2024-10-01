def total_salary(path):
    try:
        with open(path,'r') as file:

            salaries=[int(el.split(',')[1].strip()) for el in file.readlines()]
            return (sum(salaries),sum(salaries)/len(salaries))
        
    except FileNotFoundError:
        return('FILE NOT FOUND')
    except OSError or IOError:
        return('CANT READ FILE')
    
def main():
    total, average = total_salary('salaries.txt')
    print(f"Загальна сума заробітної плати: {total},\nСередня заробітна плата: {average}")

if __name__=="__main__":
    main()