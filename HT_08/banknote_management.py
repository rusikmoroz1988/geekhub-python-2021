import csv

def show_banknotes():
    with open("banknote.csv", encoding='utf-8') as r_file:
      file_reader = csv.DictReader(r_file, delimiter = ",")
      for row in file_reader:
          print(f'banknote: {row["banknote"]} count: {row["count"]}\n', end='')

def change_banknotes(list_banknot):
    names = ["banknote", "count"]
    with open("banknote.csv", mode="w", encoding='utf-8') as w_file:
        file_writer = csv.DictWriter(w_file, delimiter = ",", 
                                lineterminator="\r", fieldnames=names)
        file_writer.writeheader()
        for item in list_banknot:
            file_writer.writerow(item) 

def issued_banknotes(balance):
    with open("banknote.csv", encoding='utf-8') as r_file:
      file_reader = csv.DictReader(r_file, delimiter = ",")
      my_list = list(file_reader)
      my_list = [dict([a, int(x)] for a, x in b.items()) for b in my_list]
      my_list = sorted(my_list, key=lambda k: k['banknote'], reverse=True)
      
      list_counts = []
      last = 0
      while balance > 0:    
          for item in my_list:
              count = item['count']
              banknote = item['banknote']
              if count == 0 or banknote == last:
                  continue
              cel = balance//banknote
              if cel == 0:
                  continue
              else:
                  if cel > count:
                      balance -= count * banknote
                      while count > 0:
                        list_counts.append(banknote)
                        count-=1                                    
                  else:
                      balance -= cel * banknote
                      while cel > 0:
                          list_counts.append(banknote) 
                          cel-=1
         
          if balance>0 and len(list_counts)!=0:
              last = list_counts.pop()
              balance = last + balance
                
    return list_counts
                      