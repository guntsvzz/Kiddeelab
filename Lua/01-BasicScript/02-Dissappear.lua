-- reference
-- https://create.roblox.com/docs/tutorials/scripting/basic-scripting/intro-to-scripting

-- script.Parent is used to find the object the script is located in. 
-- As you might have guessed, script refers to the script you're writing in and the Parent of the script is where it's located.
local platform = script.Parent 
-- The CanCollide property determines if other parts (and users) can pass right through the part. 
--If you set it to false, users will fall through the platform.
local function disappear() 
	platform.CanCollide = false
	platform.Transparency = 1
end

local function appear()
	platform.CanCollide = true
	platform.Transparency = 0
end

while true do
	wait(3)
	disappear() 
	wait(3)
	appear()
end