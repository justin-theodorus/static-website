from textnode import *

def main():
    dummy = TextNode('this is some anchor text', TextType.LINK, 'https://www.boot.dev')
    print(dummy)
main()