# StackDeck.dev
StackDeck is a web platform that helps developers search for companies based on their tech stack.

![Demo](static/images/stackdeck_demo.gif)



## **About**

---
### What?
StackDeck allows you to search companies based on their tech stack, compare different stacks and analyze popularity of different frameworks.

### How?
Stackdeck facilitates two modes of interaction.
- Frontend
- API

The frontend is purely for illustration purposes and has limited functionality.


## **StackDeck API**

---

### Examples
Sample Request:
```python
import requests

company_name = "Monty Python"
url = f"https://stackdeck.dev/cards/?name={company_name}"

response = requests.get(url)
print(response.json())
```
Sample  Response:
```json
{
  "name": "Monty Python",
  "location": [
    "Camelot"
  ],
  "stack": [
    "Graham Chapman",
    "Holly Hand Grenade",
    "John Cleese"
  ],
  "flavor": "You've got two empty halves of coconuts and your bangin'em together.",
  "website": "https://en.wikipedia.org/wiki/Monty_Python",
  "tags": [],
  "alt_link": "",
  "premium": false
}
```
More detailed examples can be found in the WIKI:

[![STACKDECK](https://img.shields.io/badge/Stackdeck-WIKI-0088CC?style=for-the-badge&logo=fastapi&logoColor=white)](https://github.com/Geometrein/stackdeck/wiki)

You can check out the docs and all available methods here:

[![STACKDECK](https://img.shields.io/badge/stackdeck-docs-0088CC?style=for-the-badge&logo=fastapi&logoColor=white)](https://stackdeck.dev/docs)


## **Contributing**

---

### How to add companies?
1) **[Fork](https://github.com/Geometrein/stackdeck/fork)  the project.**
2) **Edit the `deck.json` file located in the `data` folder.**
   1) Make sure the company you're adding is not already present.
   2) Make sure the framework names are consistent with the existing ones.
   3) Each company is assigned a random 10 character ID.
3) **Submit a pull request.** 
   1) Ideally, include a link so that the added information can be verified.<br>For example, you could link to your linkedin that shows you have worked in the company that you added/modified.


[![PR](https://img.shields.io/badge/Sample_Pull_Request-0088CC?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Geometrein/stackdeck/pulls)


## Notes:

---
- Why JSON? The fact that JSON is human-readable makes adding companies easy. No need for dedicated UI and overkill databases.
- I do not consider myself an API expert, and I am open to learning.
- **Suggestions and Pull Requests are very welcome!**
