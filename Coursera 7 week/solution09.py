# Каждый из N школьников некоторой школы знает Mᵢ языков. Определите, какие языки знают
# все школьники и языки, которые знает хотя бы один из школьников.
students = [{input() for j in range(int(input()))}
            for i in range(int(input()))]
universal_language = set.intersection(*students)
someone_language = set.union(*students)
print(len(universal_language), *sorted(universal_language), sep='\n')
print(len(someone_language), *sorted(someone_language), sep='\n')
