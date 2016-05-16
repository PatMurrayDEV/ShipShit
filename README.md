
<h3 align="center">
  <img src="shpishit-icon.png" alt="🚀💩  Logo" />
</h3>
[![Twitter: @_patmurray](https://img.shields.io/badge/contact-@_patmurray-blue.svg?style=flat)](https://twitter.com/_patmurray)


### Remind yourself to come back to the hacks you shipped

When you add a hack to a project that you need to return to, add 🚀💩 to the commit message. Then an issue will be automatically created to remind you to come back and fix the hack. 

```
git commit -m "🚀💩"
```


## Set up

Set up is super easy, I'm sure you could work it out. Otherwise here's some detailed steps if you need a hand. 

#### Step 1: Get a Personal Access Token

- Go to GitHub **Settings** → **Personal access tokens** [[Direct Link](https://github.com/settings/tokens/new)] 
- Generate a new access token. 
- Grant it 'repo' access.
- Copy token to clipboard (this is the only chance you get to copy it!).

#### Step 2: Deploy to Heroku

Deploy directly to Heroku with the button below:

<p align="center">
  <a href="https://heroku.com/deploy?template=https://github.com/PatMurrayDEV/ShipShit/tree/heroku"><img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy" /></a>
</p>


Enter your Github username for `GITHUB_USERNAME` and personal access token for `GITHUB_TOKEN`. Your real password does work here, however that would be a very silly thing to put in there, you **should definitely use a personal access token**. 

#### Step 3: Set up Webhook

- Go to the Settings for your repo  
  (unfortunately you need to do this for each repo, for organisations you can set this for all repos in the Organisation settings).
- Go to **Webhooks & Services**
- Select **Add Webhook**
- For **Payload URL** enter your Heroku instance's URL with the path `/webhook`  
  (e.g., `https://secret-river-38446.herokuapp.com/webhook`)
- For **Which events would you like to trigger this webhook?**, select **Send me everything.**
- Select Add Webhook

#### Step 4: Test Webhook

When you created the webhook GitHub will test it by firing a test POST at the endpoint. In the webhooks page in GitHub it should be returning `200 OK` from your ShipShit instance. 

Now visit your Heroku instance in a webbrowser (e.g., `https://secret-river-38446.herokuapp.com/`) and you should see a test webhook successful message. This will only stay there until Heroku sleeps the server, so I reccommend you check it within half an hour (the sleep time on free Heroku instances). 


#### Step 5: Commit some 💩

Follow the usage guide below and enjoy keeping track of your hacks!


[For customisaton instruction see below]


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









