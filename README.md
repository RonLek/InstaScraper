# InstaScraper
InstaScraper downloads all images of a private profile you follow or of any public profile on Instagram and saves it on your computer.

## How to use InstaScraper?

### Customizing the script

#### Step 1
Open `scraper.py` in an editor.

#### Step 2
Provide the location of your Chrome Webdriver.`(Line 40)`

#### Step 3
Provide link of the Instagram account that you want to scrape images off. `(Line 45)`.

#### Step 4 (Optional)
If you feel you have a fast Internet connection, change `SCROLL_PAUSE_TIME` on `line 9` from `5` to `1`.

#### Step 4
Run the script!

### Running the script

#### Step 1
Run the script. A Chrome browser window opens with the Instagram homepage.

#### Step 1b(Optional)
You have 30 seconds to enter your username and password if the profile you want to scrape images off is private (You should be following the profile). If the profile is open move on to the next step.

#### Step 2
The target Instagram profile now opens. The script automatically scrolls through all the images in the profile and once it has reached the end it stores the images on your machine.

The images are stored on the path `C:\\ InstaScraper`.
