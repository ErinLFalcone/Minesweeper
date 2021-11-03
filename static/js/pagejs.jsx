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
                tile_y: cords[1],
                flag: "False"
            };
            $.get('/tile_data', tileData, res => {
                for (const tile of res) {
                    $(`#${tile[0]}-${tile[1]}`).text(tile[2]);
                    $(`#${tile[0]}-${tile[1]}`).prop("disabled",true);
                    
                }
                if ($(".tile:contains('💥')").length > 0) {
                    props.winLoseSetter('lose')
                }
            })
            ;
    } 

    const getFlag = cords => {
        const tileData = {
            tile_x: cords[0],
            tile_y: cords[1],
            flag: "True"
        };
        $.get('/tile_data', tileData);
        
        $(`#${cords[0]}-${cords[1]}`).text("🚩");
        
        const flagTiles = $(".tile:contains('🚩')");
        
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
            
        console.log(allFlags)
        console.log(props.allMines)

            if (props.allMines == allFlags) {
                props.winLoseSetter('win')
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
            <Tiles row={currRow[0]} toggleState={props.toggleState} allMines={props.allMines} mineSetter={props.mineSetter} winLoseSetter={props.winLoseSetter}/>
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
                Current Click Mode: Uncover Tiles<br></br>
                Click Here to Place Flags
                </button>
    ]


    return <section id="toggSec">{theToggler}</section>
}

const WinLose = props => {

    if (props.winLoseState === 'game') {
        return null;
    }

    let winLoseMessage = 'Reset'
    $.get('/win_lose', {win_state: props.winLoseState});
    if (props.winLoseState === 'win') {
        winLoseMessage = "Congratulations, you've won!" 
    } else if (props.winLoseState === 'lose') {
        winLoseMessage = "Sorry, you've lost!" 
    };


    return (
        <form
        action='/'
        className='winLose'
        key='winLose'
        id='winLose'
        >
            <button
                type='submit'
                className='resetButton' 
                key='resetButton' 
                id='resetButton' 
                >
                    {winLoseMessage}<br/>Click here to return to the main page!
            </button>
        </form>
    )
}

const Minesweeper = props => {

    const [toggleState, setToggleState] = React.useState(false);
    const [mineTiles, setMineTiles] = React.useState([]);
    const [winLoseState, setWinLoseState] = React.useState("game");
    const [firstOpen, setFirstOpen] = React.useState(true);

    if (firstOpen == true) {
        $.get('/read_viewed_tiles', res => {
            if (res != []) {
                for (const tile of res) {
                    $(`#${tile[0]}-${tile[1]}`).text(tile[2]);
                    if (tile[2] != "🚩") {
                        $(`#${tile[0]}-${tile[1]}`).prop("disabled",true)
                    };
                    setFirstOpen(false);
            };
        }});
}


    const toggler = () => {
        setToggleState(!toggleState)
        if (toggleState) {
            $('#flagToggle').html("Current Click Mode: Uncover Tiles<br/>Click Here to Place Flags")
        } else {
            $('#flagToggle').html("Current Click Mode: Place Flag<br/>Click Here to Uncover Tiles")
        }
    };

    const mineSetter = () => {
        $.get('/all_mines', res => {
            setMineTiles(JSON.stringify(res.sort()))
        });
    }

    const winLoseSetter = (gamestate="game") => {
        setWinLoseState(gamestate)
    };

    return (
        <div
        id="minesweeper">
            <div
            id="toggleDiv">
                <ToggleButton toggleState={toggleState} toggler={toggler}/>
            </div>
            <div
            id="container">
                <WinLose winLoseState={winLoseState}/>
                <Rows toggleState={toggleState} allMines={mineTiles} mineSetter={mineSetter} winLoseSetter={winLoseSetter} />
            </div>
        </div>
    )
}

ReactDOM.render(<Minesweeper/>, document.querySelector('#base'))
