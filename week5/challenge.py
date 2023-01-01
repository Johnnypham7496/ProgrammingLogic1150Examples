def star_id(id):
    if len(id) >= 8:
        return True
    else:
        return False

def main():
    id = 'kittens'
    print(star_id(id))

main()