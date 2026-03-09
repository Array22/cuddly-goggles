

const stockGrowth = document.querySelector("#stock-growth");
const growthValue = parseFloat(stockGrowth.textContent);

if (growthValue > 0) {
    stockGrowth.classList.add("text-green-600")
} else if (growthValue < 0) {
    stockGrowth.classList.add("text-red-600")
}

const btnStockAdd = document.querySelector("#stock-add");
const chartTemplate = document.querySelector("#chart-widget");
const widgetContainer = document.querySelector("#widget-container");

function addWidget() {
    const clone = chartTemplate.content.cloneNode(true);
    widgetContainer.appendChild(clone);
}

const btnChartClose = document.querySelector("#chart-close");

function closeWidget(clickEvent) {
    if (clickEvent.target.matches("#chart-close")) {
        clickEvent.target.closest(".tradingview-widget-container").remove();
    }
}



//event listeners
btnStockAdd.addEventListener("click", addWidget);
widgetContainer.addEventListener("click", closeWidget);