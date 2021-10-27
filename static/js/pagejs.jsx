'use strict';

// 30x20

const tileArray = [];
for (let iy = 0; iy<=19; iy+=1) {
    tileArray.push([iy])
    for (let ix = 0; ix<=29; ix+=1 ) {
        if (ix === 0) {
            tileArray[iy].push([ix])
        };
        if (ix !== 0) {
            tileArray[iy][1].push(ix)
        };
        };
}

const Tiles = props => {

    const getTile  = cords => {
            const tileData = {
                tile_x: cords[0],
                tile_y: cords[1]
            };
            $.get('/tile_data', tileData, res => {
                for (const tile of res) {
                    $(`#${tile[0]}-${tile[1]}`).text(tile[2])
                }  
            });
    } 

    const getFlag = cords => {
        $(`#${cords[0]}-${cords[1]}`).text("F");
        
        const flagTiles = $(".tile:contains('F')");
        
        const flagIds = []

        for (const tile of flagTiles) {
            
            let tileCords = tile.id.split("-")
            for (const i in tileCords) {
                tileCords[i] = parseInt(tileCords[i])
            }
            flagIds.push(tileCords)
        }  

        if ((props.allMines).length < 1) {
            props.mineSetter()
        };
        
        const allFlags = JSON.stringify(flagIds.sort());
            
            if (props.allMines == allFlags) {
                console.log("You win!")
            } else {
                console.log("allFlags = ", allFlags)
                console.log("allMines = ", props.allMines)
            };
    }

    const toggClick = cords => {
        if (props.toggleState) {
            getFlag(cords)
        } else {
            getTile(cords)
        };
    };

    const tileBttns = []
    for (const currTile of tileArray[0][1]) {
        tileBttns.push(
            <button
             type="button"
             className="tile" 
             key={`${currTile}-${props.row}`} 
             id={`${currTile}-${props.row}`} 
             onClick={() => toggClick([currTile,props.row])}>⠀</button> 
        )
    }

    return <section className="row">{tileBttns}</section>

}

const Rows = props => {

    const rowArray = []

    for (const currRow of tileArray) {
        rowArray.push(
            <div
            className='row'
            key={`row-${currRow[0]}`}
            id={`row-${currRow[0]}`}
            >
            <Tiles row={currRow[0]} toggleState={props.toggleState} allMines={props.allMines} mineSetter={props.mineSetter}/>
            </div>
        )
    }
    return <section className="map">{rowArray}</section>

}

const ToggleButton = props => {

    const theToggler = [
        <button
                type="button"
                className="flagToggle"
                key="flagToggle"
                id="flagToggle"
                onClick={() => props.toggler()}
                >
                Place Flag Toggle</button>
    ]


    return <section id="toggSec">{theToggler}</section>
}

const Minesweeper = props => {

    const [toggleState, setToggleState] = React.useState(false);
    const [mineTiles, setMineTiles] = React.useState([]);


    const toggler = () => {
        setToggleState(!toggleState)
        console.log(toggleState)
    };

    const mineSetter = () => {
        $.get('/all_mines', res => {
            console.log(res)
            setMineTiles(JSON.stringify(res.sort()))
        });
    }

    return (
        <div
        id="minesweeper">
            <div
            id="toggleDiv">
                <ToggleButton toggleState={toggleState} toggler={toggler}/>
            </div>
            <div
            id="container">
                <Rows toggleState={toggleState} allMines={mineTiles} mineSetter={mineSetter}/>
            </div>
        </div>
    )

}

ReactDOM.render(<Minesweeper/>, document.querySelector('#base'))
