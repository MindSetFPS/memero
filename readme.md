# memero:

## A meme organizer for the sophisticated memelord.

memero can be seen as a album with high focus in tags, organization and classificatinon, but also recollection of memes.

The recollector will use available api's, as well as selenium.

The album will display your memes in alphabetical order, or by popularity, with the ability of filter by tags.

The app will show the top memes found in the last 24 hours.

The app will run in a container with bot services.

Album:
    - Frontend: Built with Svelte
        - Ability of uploadig new memes
    - Backend: Built with Flask
    - Database: SQlite? Used for saving tags and routes.

Recollector:
    - Selenium

## Todo

- [x] Delete memes
- [x] Delete tags
- [ ] Filter memes by name, size, likes, number of tags (by default)
- [ ] Support for video memes
- [ ] Recollect best memes of the day
- [ ] Sort by popularity
- [ ] Select mulple memes for deletion
- [ ] Sort first memes with tags
- [ ] Analyze 'memes' in the background to add files by jus dropping them in the folder
- [ ] Group similar images
- [ ] Add a field for number of likes/upvotes/ popularity
- [ ] Built in image editor
- [ ] Fix mobile version
- [ ] Suggestions when adding a new tag
- [ ] Remove spaces in tags
- [ ] Create installable app

## Instructions for getting running

###  Start development server

```bash
flask --app app --debug run
```

## Build container
 
 ```bash
 docker build -t memerobuild:0.X -f Dockerfile.prodcontainer .
 ```

# Build Desktop app

## Create new spec

```bash
pyi-makespec --onefile --noconsole --icon clown-face.ico --name dist .\main.py
```

## Add the ui files

```
a = Analysis(
    ['main.py'],
    //other parameters
    datas=[('public','.\public')],
```

## Or use predefined spec, then run the build command

```bash
pytinstaller dist.spec
```