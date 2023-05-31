print("Hello world!")

local baseplate = game.Workspace.Baseplate
local myNumber =.5

local function MyFunction(transparency)
	baseplate.Transparency = transparency
	
end
	
print(baseplate.BrickColor)

baseplate.Transparency = myNumber

MyFunction(1)