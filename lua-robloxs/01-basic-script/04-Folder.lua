local part3Folder = workspace:WaitForChild("Part3")
--format : workspace:WaitForChild(str-namefolder)
local part3pickups = part3Folder:GetChildren()
-- Return array of that folder

--local function disappear(platform)
--	platform.CanCollide = false
--	platform.Transparency = 1
--end

--local function appear(platform)
--	platform.CanCollide = true
--	platform.Transparency = 0
--end

local function fade(platform)
	for count = 1, 10 do
		platform.Transparency = count/10
		wait(0.1)
	end
	platform.CanCollide = false
	platform.Transparency = 1
	wait(1)
	platform.CanCollide = true
	platform.Transparency = 0
	
end

--while true do
--	for _, part3pickup in ipairs(part3pickups) do
--		wait(1)
--		disappear(part3pickup)
--		wait(1)
--		appear(part3pickup)
--	end
--end

while true do
		for _, part3pickup in ipairs(part3pickups) do
			fade(part3pickup)
		end
	end