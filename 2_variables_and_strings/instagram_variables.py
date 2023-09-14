post_likes = 30

# user like this post - the value of the variable needs to be updated
post_likes = post_likes + 1

# user unlikes the post
post_likes = post_likes - 1 

# creating a message to display with the number of likes
message = f'{post_likes} likes'

print(message)


# created page title with username variable
username = 'google'

page_title = f'@{username}'


print(page_title)


# switch to a differenet username
username = 'minneapolis_college'

followers = 1522

followers = followers + 1

# Optional - :,d prints the int with variables
print(f'{followers:,d}')

# checking the length of the post text
post_text = 'I met a llama this summer'
post_text_length = len(post_text)

print(post_text_length)