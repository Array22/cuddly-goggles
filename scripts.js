

const stockGrowth = document.querySelector("#stock-growth");
const growthValue = parseFloat(stockGrowth.textContent);

if (growthValue > 0) {
    stockGrowth.classList.add("text-green-600")
} else if (growthValue < 0) {
    stockGrowth.classList.add("text-red-600")
}