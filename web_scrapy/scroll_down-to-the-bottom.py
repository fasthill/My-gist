# scroll down to the current bottom of the window
# 현재 보이는 브라우저에서 한 단계 밑으로 scroll down
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

# scroll down to the end bottom of the window
# 현재 보이는 브라우저에서 더 이상 내려 갈 곳이 없는 마지막까지 scroll down
def scroll_down_bottom():
    """A method for scrolling the page."""

    # Get scroll height.
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:

        # Scroll down to the bottom.
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load the page.
        time.sleep(2)

        # Calculate new scroll height and compare with last scroll height.
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:

            break

        last_height = new_height
        
    return True

if scroll_down_bottom():
    print("Done")
