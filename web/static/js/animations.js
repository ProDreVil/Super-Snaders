// CHECKERED BOARD ANIMATION

const directions = [
    [1, 0],    // Right
    [-1, 0],   // Left
    [0, 1],    // Down
    [0, -1],   // Up
    [1, 1],    // Down-right
    [-1, 1],   // Down-left
    [1, -1],   // Up-right
    [-1, -1]   // Up-left
];

const direction = directions[
    Math.floor(Math.random() * directions.length)
];

document.documentElement.style.setProperty(
    "--drift-x",
    `${direction[0] * 4}rem`
);

document.documentElement.style.setProperty(
    "--drift-y",
    `${direction[1] * 4}rem`
);

document.body.classList.add("background-drift");


// SCROLL FADE INDICATOR

const boardScroll = document.querySelector(".board-scroll");
const boardGrid = document.querySelector(".board-grid");

function updateBoardShadows() {
    const canScroll = boardGrid.scrollHeight > boardGrid.clientHeight + 1;
    const atBottom = boardGrid.scrollTop >= -1;
    const atTop = boardGrid.scrollTop <=
        -(boardGrid.scrollHeight - boardGrid.clientHeight) + 1;

    boardScroll.classList.toggle(
        "show-top-shadow",
        canScroll && !atTop
    );

    boardScroll.classList.toggle(
        "show-bottom-shadow",
        canScroll && !atBottom
    );
}

boardGrid.addEventListener("scroll", updateBoardShadows);
window.addEventListener("resize", updateBoardShadows);

new ResizeObserver(updateBoardShadows).observe(boardGrid);

updateBoardShadows();