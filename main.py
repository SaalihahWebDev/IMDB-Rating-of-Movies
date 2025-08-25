import matplotlib.pyplot as plt
movies=["Inception","Instellar","Dark","Titanic","Moment to reality"]
ratings=[8.8,8.6,9.0,7.4,8.4]
plt.figure(figsize=(8,5))
plt.bar(movies,ratings,color="pink")
plt.xlabel("Movies")
plt.ylabel("IMDB Rating")
plt.title("IMDB Rating of Movies")
plt.ylim(0,10)
plt.show()