import requests
from bs4 import BeautifulSoup

URL = 'http://books.toscrape.com/'
page = requests.get(URL)

soup = BeautifulSoup(page.content , 'html.parser')

#bookName = results.find( 'h1' ).text
#print( "bookName   = " + bookName )

#bookPrice = results.find( 'p' , class_ = 'price_color' ).text
#print( "bookPrice  = " + bookPrice )

#stockCount = results.find( 'p' , class_ = 'instock availability' ).text.strip()
#print( "stockCount = " + stockCount )

#rating = results.find('p' , class_ = 'star-rating').get("class")[1]
#print( "rating     = " + rating +" /five")



booksList = soup.find_all( 'li' , class_ = 'col-xs-6 col-sm-4 col-md-3 col-lg-3' )

print( "\nA scrapper which scraps from http://books.toscrape.com/\nTotal Books = " + str(len(booksList)) ) 
print()


for element in booksList:
	print("Book Name = " + element.find('h3').text)
	print("Price = " + element.find('p' , class_ = 'price_color').text)
	print("Availability = " + element.find('p' , class_='instock availability').text.strip())
	rating = element.find('p' , class_='star-rating').get("class")[1]
	print("Rating = " + rating + "/five")
	print()
	print()