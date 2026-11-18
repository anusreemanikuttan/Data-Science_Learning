

# ## Movie Rating
# ------------------------------------------------------
# Create a class Movie whose constructor accepts:
#
#  movie name
#  hero
#  rating
#
# Add a method to check:
#
#  If rating >= 7 → print “Hit movie”
#  Else → print “Average movie”
# -------------------------------------------------------
class Movie:

    def __init__(self,name,hero,rating):
        self.name = name
        self.hero = hero
        self.rating = rating
    def check(self):
        if self.rating >= 7:
            return "Hit Movie"
        else:
            return "Average Movie"

m1 = Movie("Oppenheimer","Cillian Murphy", 7)
print(m1.check())
m2 = Movie("Leo","Vijay", 6)
print(m2.check())