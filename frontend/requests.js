site = "http://localhost:8000/";

export function checkPhishing(url) {
  const site_url = `${site}phishing?url=${url}`;

  fetch(site_url)
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
    })
    .catch((error) => {
      console.error(error);
    });
}

// test
sendGetRequest(
  "https://www.goodd-gler222.co/search?q=convert+a+url+string+into+domain+name+and+tld&rlz=1C1ONGR_enNP1088NP1088&oq=convert+a+url+string+into+domain+name+and+tld&gs_lcrp=EgZjaHJvbWUyCAgAEEUYFRg5MgcIARAhGKABMgcIAhAhGKABMgcIAxAhGKAB0gEJMTQwMTFqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8"
);
