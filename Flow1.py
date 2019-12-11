[{"id":"67e7284b.324c68","type":"tab","label":"Flow 1","disabled":false,"info":""},{"id":"525b1a8c.a89b64","type":"rpi-gpio in","z":"67e7284b.324c68","name":"Button","pin":"7","intype":"up","debounce":"25","read":true,"x":240,"y":280,"wires":[["98f8c76c.678c78","c8ffd24.515f33"]]},{"id":"4642e16d.d1693","type":"rpi-gpio out","z":"67e7284b.324c68","name":"LED","pin":"11","set":true,"level":"0","freq":"","out":"out","x":730,"y":420,"wires":[]},{"id":"c8ffd24.515f33","type":"debug","z":"67e7284b.324c68","name":"","active":true,"tosidebar":true,"console":false,"tostatus":false,"complete":"false","x":460,"y":240,"wires":[]},{"id":"98f8c76c.678c78","type":"switch","z":"67e7284b.324c68","name":"if input is 1","property":"payload","propertyType":"msg","rules":[{"t":"eq","v":"1","vt":"str"},{"t":"else"}],"checkall":"true","repair":false,"outputs":2,"x":310,"y":420,"wires":[["21ffe1b3.9b7c5e"],["be1323b1.69eaf"]]},{"id":"21ffe1b3.9b7c5e","type":"change","z":"67e7284b.324c68","name":"Change to 0","rules":[{"t":"set","p":"payload","pt":"msg","to":"0","tot":"str"}],"action":"","property":"","from":"","to":"","reg":false,"x":530,"y":420,"wires":[["4642e16d.d1693"]]},{"id":"be1323b1.69eaf","type":"change","z":"67e7284b.324c68","name":"Change to 1","rules":[{"t":"set","p":"payload","pt":"msg","to":"1","tot":"str"}],"action":"","property":"","from":"","to":"","reg":false,"x":530,"y":480,"wires":[["4642e16d.d1693"]]}]
