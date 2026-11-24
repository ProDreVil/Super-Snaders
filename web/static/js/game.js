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