class Solution(object):
    def sortPeople(self, names, heights):

        sortPerson = [(names, heights) for names, heights in zip(names, heights)]
        sortPerson.sort(key=lambda x: x[1] , reverse=True)
        sorted_name = [PPL[0] for PPL in sortPerson]

        return sorted_name