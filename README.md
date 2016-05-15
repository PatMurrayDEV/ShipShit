
<h3 align="center">
  <img src="shpishit-icon.png" alt="🚀💩  Logo" />
</h3>
[![Twitter: @_patmurray](https://img.shields.io/badge/contact-@_patmurray-blue.svg?style=flat)](https://twitter.com/_patmurray)
[![Twitter: @busbub](https://img.shields.io/badge/contact-@busbub-blue.svg?style=flat)](https://twitter.com/busbub)


### Remind yourself to come back to the hacks you shipped

When you add a hack to a project that you need to return to, add 🚀💩 to the commit message. Then an issue will be automatically created to remind you to come back and fix the hack. 

```
git commit -m "🚀💩"
```

#### *This is still super early, and doesn't work (well -- it does in fact work now!). Maybe check back later* 🤗

***********



## Set up

**Easiest**: Deploy directly to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/PatMurrayDEV/ShipShit/tree/heroku)


## Usage

Usage is simple enough. Just include the string 🚀💩 in any commit message and you'll get a GitHub issue created to remind you to fix it later. 

```
git commit -m "🚀💩"
```
```
git commit -m "🚀💩: created a UISearchController that works, but is a total hack"
```
```
git commit -m "things are less shitty than before - 🚀💩"
```
```
git commit -m "i really 🚀💩 on this one"
```

#### Alternatives?
Don't support emoji? You can use the phrase `shipshit` (case insensitive) as an alternative.

```
git commit -m "shipshit"
```
```
git commit -m "shipshit: created a UISearchController that works, but is a total hack"
```
```
git commit -m "things are less shitty than before - shipshit"
```
```
git commit -m "i really shipshit on this one"
```
*(See, not as fun as the emoji)*

## Development

To develop, install the dependency packages through pip:

`pip install -r requirements.txt`

Then run main.py

To add new dependencies, just update the requirements.txt using

`pip freeze > requirements.txt`

Note: this is obviously oversimplified. Be prudent when adding new dependencies.

## Variables 

[To Come]

## License

MIT, see LICENSE file. *(If this is a bad choice of license, tell me… I have no idea 😝)*



## Credits

- Pat Murray — [@_patmurray](https://twitter.com/_patmurray)
- Mitch Busby — [@busbub](https://twitter.com/busbub)









