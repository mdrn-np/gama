server_url = "http://localhost:8000/";

export async function checkPhishing(url) {
  const site_url = `${server_url}phishing?url=${url}`;

  await fetch(site_url)
    .then((response) => response.json())
    .then((data) => {
      return data;
    })
    .catch((error) => {
      console.error(error);
    });
}

// test
console.log(
  checkPhishing(
    "https://www.goodd-gler222.co/search?q=convert+a+url+string+into+domain+name+and+tld&rlz=1C1ONGR_enNP1088NP1088&oq=convert+a+url+string+into+domain+name+and+tld&gs_lcrp=EgZjaHJvbWUyCAgAEEUYFRg5MgcIARAhGKABMgcIAhAhGKABMgcIAxAhGKAB0gEJMTQwMTFqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8"
  )
);
export async function getWebDetails(url) {
  const site_url = `${server_url}details?url=${url}`;

  await fetch(site_url)
    .then((response) => response.json())
    .then((data) => {
      return data;
    })
    .catch((error) => {
      console.error(error);
    });
}

// test
console.log(getWebDetails("theintercept.com")); // dnssec is true
console.log(getWebDetails("google.com")); // dnssec is false
