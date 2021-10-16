'use strict';

// 30x20

const Tiles = props => {
    const [tileId, setTileId] = React.useState([0,0]);
    const tileArray = [];
    for (let iy = 1; iy<=20; iy+=1 ) {
        for (let ix = 1; ix<=30; ix+=1 ) {
            let xy = ([ix,iy])
            tileArray.push(xy);
    }
    }
    const getTile  = currTile => {
            console.log(currTile)
            const tileData = {
                tile_x: currTile[0],
                tile_y: currTile[1]
            };
            $.get('/tile_data', tileData, res => {
                console.log(res)
                return res
            });
    } 


    const tileImgs = []
    for (const currTile of tileArray) {
        // setTileId(currTile);
        
        tileImgs.push(
            <img className="tile" 
             key={`[${currTile[0]},${currTile[1]}]`} 
             id={`[${currTile[0]},${currTile[1]}]`} 
             src='static/img/testbox.jpg'
             onClick={() => getTile(currTile)}></img> 
        )
        // setTileId([0,0]);
    }


    return <section className="map">{tileImgs}</section>

}   

ReactDOM.render(<Tiles/>, document.querySelector('#container'))


