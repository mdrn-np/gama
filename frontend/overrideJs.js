let reportBtn = document.getElementById("reportBtn");
reportBtn.addEventListener("click", () => {
  reportBtn.disabled = true;
});
document.getElementById("proceedBtn").addEventListener("click", function () {
  window.history.go(-1);
  return false;
});
