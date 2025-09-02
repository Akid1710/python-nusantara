def say_hello(name):
    #
    #
    print(f"Halo Mr.{name}")
    print("Baek Baek Aeeee")

#
#
say_hello_mini = lambda name : print(f"Hallo Mr.{name}")
#
say_hello("Dika")
say_hello("Shaqila")
say_hello_mini("Akid")
say_hello_mini("Qila")

#map()----sorter()----filter()
jajan_mingguan=[10000,50000,1000000,45000]
urutkan_uang= sorted(jajan_mingguan)
urutkan_uang_terbalik= sorted(jajan_mingguan,reverse=True)
print(f"urutkan uang: {urutkan_uang}")
print(f"urutan uang terbalik: {urutkan_uang_terbalik}")

kurangin_uang= map(lambda uang:uang -5000, jajan_mingguan)
list_kurangin_uang = list(kurangin_uang)
print(f"map uang berkurang: {list_kurangin_uang}")