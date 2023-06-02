-- reference
-- https://create.roblox.com/docs/tutorials/first-experience

print("Hello world!") --Basic Print

local baseplate = game.Workspace.Baseplate -- Calling Baseplate inside Workspace
local myNumber  = .5 -- variable
-- Format : local function FunctionName(*agrument)
local function MyFunction(transparency) 
	baseplate.Transparency = transparency 
end
-- Transparency is one of properties inside Baseplate	
print(baseplate.BrickColor) -- showing in output
-- new value properties
baseplate.Transparency = myNumber
--or
MyFunction(.5)