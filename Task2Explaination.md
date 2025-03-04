<h1>Book Inventory Management System</h1>

<h2>Overview</h2>
<p>This project is a <strong>Book Inventory Management System</strong> implemented in Python. 
It allows users to manage book details, search books by author, update book prices, standardize genres, 
display inventory in a tabular format, and list all book titles.</p>

<h2>Features</h2>
<ul>
    <li><strong>Create an Inventory</strong>: Store books using ISBN as the key.</li>
    <li><strong>Search by Author</strong>: Retrieve all books written by a specific author.</li>
    <li><strong>Update Book Price</strong>: Modify the price of a book using its ISBN.</li>
    <li><strong>Standardize Genres</strong>: Format all genres in lowercase and remove extra spaces.</li>
    <li><strong>Display Inventory</strong>: Print book details in a structured table format.</li>
    <li><strong>List All Book Titles</strong>: Get a sorted list of all book titles.</li>
</ul>

<hr>

<h2>Tasks Implemented</h2>

<h3>Task 1 - Part 1: Create an Empty Dictionary</h3>
<p>The inventory is implemented as a dictionary with ISBN as the key, and each value is a tuple containing:</p>
<ul>
    <li><strong>Title</strong> (string)</li>
    <li><strong>Author</strong> (string)</li>
    <li><strong>Price</strong> (float)</li>
    <li><strong>Genres</strong> (set of strings)</li>
</ul>

<pre><code># Step 1: Create an empty dictionary
inventory = {}

# Step 2: Add books with ISBN as keys and details as tuples
inventory["9780439136365"] = ("", "J.K. Rowling", 25.99, {"fantasy", "adventure"})
inventory["9780307277671"] = ("To Kill a Mockingbird", "Harper Lee", 18.99, {"history", "non-fiction"})
inventory["9780140449136"] = ("The Republic", "Plato", 10.99, {"philosophy", "politics"})
inventory["9780743273565"] = ("The Great Gatsby", "F. Scott Fitzgerald", 15.50, {"classic", "fiction"})
inventory["9780262033848"] = ("Time to Love", "Michael Sipser", 60.99, {"computer science", "mathematics"})

# Step 3: Display the inventory dictionary
inventory</code></pre>

<h3>Task 1 - Part 2: Search Book by Author</h3>
<p>Function <code>search_by_author(author)</code>:</p>
<ul>
    <li>Loops through the inventory.</li>
    <li>Finds books by the given author.</li>
    <li>Returns a list of (ISBN, Title) pairs.</li>
    <li>Handles cases where no books are found.</li>
</ul>

<pre><code>def search_by_author(author):
    result = [(isbn, details[0]) for isbn, details in inventory.items() if details[1].lower() == author.lower()]
    return result

# Example Usage
search_results = search_by_author("J.K. Rowling")
print(search_results)
</code></pre>

<h3>Task 1 - Part 3: Update Book Price</h3>
<p>Function <code>update_price(isbn, new_price)</code>:</p>
<ul>
    <li>Checks if ISBN exists.</li>
    <li>Creates a new tuple with the updated price.</li>
    <li>Replaces the old entry in the dictionary.</li>
</ul>

<pre><code>
  def update_price(isbn, new_price):
    if isbn in inventory:
        title, author, _, genres = inventory[isbn]  # Unpack existing values
        inventory[isbn] = (title, author, new_price, genres)  # Create new tuple with updated price
        return f"Price updated for ISBN {isbn} to ${new_price:.2f}"
    else:
        return f"ISBN {isbn} not found in inventory."

print(update_price("9780439136365", 30.99))
print(update_price("1234567890", 19.99))
</code></pre>

<h3>Task 1 - Part 4: Standardize Book Genres</h3>
<p>Function <code>standardize_genres()</code>:</p>
<ul>
    <li>Iterates over all books in the inventory.</li>
    <li>Formats all genre strings to lowercase and removes extra spaces.</li>
</ul>

<pre><code>for isbn, details in inventory.items():
        title, author, price, genres = details
        cleaned_genres = {genre.strip().lower() for genre in genres}  # Clean each genre
        inventory[isbn] = (title, author, price, cleaned_genres)  # Update tuple

standardize_genres()</code></pre>

<h3>Task 1 - Part 5: Display Inventory</h3>
<p>Function <code>display_inventory()</code>:</p>
<ul>
    <li>Loop through the inventory dictionary.</li>
    <li>Print out the details of each book in a clean table format.</li>
</ul>

<pre><code>def display_inventory():
    print(f"{'ISBN':<20} {'Title':<35} {'Author':<25} {'Price':<10} {'Genres'}")
    print("=" * 100)

    for isbn, (title, author, price, genres) in inventory.items():
        genres_str = ", ".join(genres)  # Convert genres set to a string
        print(f"{isbn:<20} {title:<35} {author:<25} ${price:<10.2f} {genres_str}")

# Example Usage
display_inventory()</code></pre>

<h3>Task 1 - Part 6: List All Book Titles</h3>
<p>Function <code>list_all_books()</code>:</p>
<ul>
    <li>Returns a sorted list of book titles.</li>
</ul>

<pre><code>def list_all_books():
    return sorted([details[0] for details in inventory.values()])  # Extract titles & sort
print(list_all_books())</code></pre>
<hr>

<h2>Installation & Usage</h2>
<h3>Prerequisites</h3>
<ul>
    <li>Python 3.x</li>
    <li>Install dependencies</li>
</ul>

<h3>How to Run</h3>
<ol>
    <li>Clone the repository:</li>
</ol>

<pre><code>git clone https://github.com/faisalrafique031/python-al-junaid-tech.git
cd Python-Al-Junaid-Tech</code></pre>

<ol>
    <li>Run the script:</li>
</ol>

<pre><code>python Task2.ipynb
OR
Task2.py  # if using simple python not jupyter
</code></pre>

<p>Follow on-screen instructions to manage book inventory.</p>

<hr>

<h2>Example Usage</h2>

<pre><code># Adding books to inventory
inventory["9780399164059"] = ("The Hobbit", "J.R.R. Tolkien", 12.99, {"fantasy", "adventure"})
inventory["9780452284234"] = ("To Kill a Mockingbird", "Harper Lee", 9.99, {"classic", "historical"})

# Search for books by author
print(search_by_author("Harper Lee"))

# Update book price
update_price("978-0-399-16405-9", 15.99)

# Display inventory
display_inventory()

# List all book titles
print(list_all_books())</code></pre>

<hr>

<h2>Contributing</h2>
<ul>
    <li>Fork the repository.</li>
    <li>Create a new branch.</li>
    <li>Submit a pull request.</li>
</ul>

<hr>

<h2>License</h2>
<p>This project is licensed under the <strong>MIT License</strong>.</p>

<hr>

<h2>Author</h2>
<p><strong>Your Name</strong> (GitHub: <a href="https://github.com/faisalrafique031">Faisal Rafiq</a>)</p>

</body>
</html>
