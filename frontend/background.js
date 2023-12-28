const server_url = "http://localhost:8000/";
let activeTabUrl = "";
let onoffstate;
chrome.runtime.onMessage.addListener(function (message, sender, sendResponse) {
  onoffstate = message.checkboxState;
});

chrome.tabs.onUpdated.addListener(async () => {
  if (onoffstate == "unchecked") {
    // returns active tab's url
    chrome.tabs.query({ highlighted: true }, async (tabs) => {
      let activeTab = tabs[0];
      activeTabUrl = activeTab.url;
      console.log(activeTabUrl);

      async function checkPhishing(url) {
        try {
          const response = await fetch(url);
          const data = await response.json();
          return data;
        } catch (error) {
          console.log(error);
          return false;
        }
      }
      let phishing_url = `${server_url}phishing?url=${activeTabUrl}`;
      phishing = await checkPhishing(phishing_url);

      // In background.js
      if (phishing) {
        var url = "override.html?url=" + encodeURIComponent(activeTabUrl);
        chrome.tabs.update({ url: url });
      }
      console.log(phishing);
    });
  }
});

chrome.runtime.onInstalled.addListener(() => {
  // adds context menu needed for our extension on installation
  chrome.contextMenus.create({
    id: "review_check",
    title: "Review Check",
    contexts: ["selection"],
  });
  chrome.contextMenus.create({
    id: "news_check",
    title: "News Check",
    contexts: ["selection"],
  });
  console.log("test");
});

chrome.contextMenus.onClicked.addListener((clickData) => {
  // extracts the selected / highlighted value
  if (clickData.menuItemId == "review_check" && clickData.selectionText) {
    let review = clickData.selectionText;
    const review_url = `${server_url}review`;

    let reviewData = {
      review: `${review}`,
    };

    fetch(review_url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(reviewData),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(data.prediction);

        chrome.notifications.create("installation", {
          type: "basic",
          iconUrl: "logo.png",
          title: "Review Validation",
          message: data.prediction
            ? "The review is likely fake (take it with a grain of salt)"
            : "The review is authentic",
          priority: 1,
        });
      })
      .catch((error) => console.log(error));
    console.log(review);
  } else if (clickData.menuItemId == "news_check" && clickData.selectionText) {
    let news = clickData.selectionText;
    const news_url = `${server_url}news`;
    let newsData = {
      news: `${news}`,
    };
    fetch(news_url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(newsData),
    })
      .then((response) => response.json())
      .then((data) => {
        chrome.notifications.create("installation", {
          type: "basic",
          iconUrl: "logo.png",
          title: "News Validation",
          message:
            data.prediction == "REAL"
              ? "The News is likely authentic"
              : "The News is likely fake (fact checking is recommonded)",
          priority: 1,
        });
      })
      .catch((error) => console.log(error));
    console.log(news);
  }
});
