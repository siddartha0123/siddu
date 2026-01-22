let quoteTxt = document.getElementById("quote-txt");
const btn = document.querySelector("#btn");
const textGenerate = async () => {
  quoteTxt.textContent = "Generting text wait plz ....";
  try {
    res = await fetch("http://127.0.0.1:8000/", {
      method: "POST",
    });
    data = await res.json();
    console.log(data);
    quoteTxt.textContent = data.quote;
  } catch (err) {
    console.error(err);
  }
};

btn.addEventListener("click", textGenerate);
