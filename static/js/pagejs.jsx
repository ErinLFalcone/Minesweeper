'use strict';

// 30x20

// [[0, [0,1,2,3,4]], [1,[0,1,2,3,4]], [2,[0,1,2,3,4]]]

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
            console.log(cords)
            console.log(cords[0])
            const tileData = {
                tile_x: cords[0],
                tile_y: cords[1]
            };
            $.get('/tile_data', tileData, res => {
                console.log(res)
                for (const tile of res) {
                    $(`#-${tile[0]}-${tile[1]}-`).text(tile[2])
                }
                
            });
    } 

    const tileBttns = []
    for (const currTile of tileArray[0][1]) {
        tileBttns.push(
            <button
             type="button"
             className="tile" 
             key={`-${currTile}-${props.row}-`} 
             id={`-${currTile}-${props.row}-`} 
             onClick={() => getTile([currTile,props.row])}> </button> 
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
            <Tiles row={currRow[0]}/>
            </div>
        )
    }
    return <section className="map">{rowArray}</section>

}

ReactDOM.render(<Rows/>, document.querySelector('#container'))


