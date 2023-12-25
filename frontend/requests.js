site = "http://localhost:8000/";

async function checkPhishing(url) {
  const site_url = `${site}phishing?url=${url}`;

  await fetch(site_url)
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
    })
    .catch((error) => {
      console.error(error);
    });
}

// test
checkPhishing(
  "https://www.goodd-gler222.co/search?q=convert+a+url+string+into+domain+name+and+tld&rlz=1C1ONGR_enNP1088NP1088&oq=convert+a+url+string+into+domain+name+and+tld&gs_lcrp=EgZjaHJvbWUyCAgAEEUYFRg5MgcIARAhGKABMgcIAhAhGKABMgcIAxAhGKAB0gEJMTQwMTFqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8"
);
async function getWebDetails(url) {
  const site_url = `${site}details?url=${url}`;

  await fetch(site_url)
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
    })
    .catch((error) => {
      console.error(error);
    });
}

// test
getWebDetails("theintercept.com"); // dnssec is true
getWebDetails("google.com"); // dnssec is false
