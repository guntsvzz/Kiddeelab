Gun
Gun#4823

Gun — Today at 4:15 PM
Players = game:GetService("Players")
Players.PlayerAdded:Connect(function(player)
    -- printing starter joining
    print(player.Name .. " joined the game!")

    local folder = Instance.new("Folder", player)
    folder.Name = player.Name

end)

Players.PlayerRemoving:Connect(function(player)
    -- printing when stop game
    print(player.Name .. " left the game!")
end)
local function onPlayerAdded(player)
    print(player)
    local leaderstats = Instance.new("Folder")
    leaderstats.Name = "leaderstats"
    leaderstats.Parent = player

    local points = Instance.new("IntValue")
    points.Name = "Points"
    points.Value = 0
    points.Parent = leaderstats
end
Players.PlayerAdded:Connect(onPlayerAdded)
local MAX_HEALTH = 100
local ENABLED_TRANSPARENCY = 0.4
local DISABLED_TRANSPARENCY = 0.9
local COOLDOWN = 10

local healthPickupsFolder = workspace:WaitForChild("HealthPickups")
local healthPickups = healthPickupsFolder:GetChildren()

local function onTouchHealthPickup(otherPart, healthPickup)
    if healthPickup:GetAttribute("Enabled") then

        local playerList = Players:GetPlayers()
            for i = 1, #playerList  do
                local player = playerList[i]
                if player then
                    local points = player.leaderstats.Points
                    points.Value = points.Value + 1
                end
            end

        local character = otherPart.Parent
        local humanoid = character:FindFirstChildWhichIsA("Humanoid")
        if humanoid then
            print(humanoid)
            humanoid.Health = MAX_HEALTH
            healthPickup.Transparency = DISABLED_TRANSPARENCY
            healthPickup:SetAttribute("Enabled", false)
            task.wait(COOLDOWN)
            healthPickup.Transparency = ENABLEDTRANSPARENCY
            healthPickup:SetAttribute("Enabled", true)
        end
    end
end

for , healthPickup in ipairs(healthPickups) do
    healthPickup:SetAttribute("Enabled", true)
    healthPickup.Touched:Connect(function(otherPart)
        onTouchHealthPickup(otherPart, healthPickup)
    end)
end
Gun — Today at 5:49 PM
--Creating Folder inside workspace
local circleFolder = Instance.new("Folder")
circleFolder.Name = "Circles"
circleFolder.Parent = workspace

--creating 10 plate
Expand
platenocode.txt
2 KB
﻿
seasorn
seasorn#3985
--Creating Folder inside workspace
local circleFolder = Instance.new("Folder")
circleFolder.Name = "Circles"
circleFolder.Parent = workspace

--creating 10 plate
numPlate = 10 
local circleRadius = 1
local circlecolor = BrickColor.new("Bright red")
for i = 1, numPlate do	
	local circle = Instance.new('Part')
	circle.Shape = Enum.PartType.Ball
	circle.Parent = game.Workspace
	circle.BrickColor = circlecolor
	circle.Size = Vector3.new(circleRadius, circleRadius, circleRadius)
	circle.CanCollide = true
	circle.Position = Vector3.new((i+1)*10,0,0)
	-- Insert the circle back to Workspace
	circle.Parent = circleFolder
end

-- calling array
--local circleFolder = workspace:WaitForChild(circleFolder.Name)
local eachcircle = circleFolder:GetChildren()
--print(eachcircle)
--for _, cir in ipairs(eachcircle) do
--	print(cir)
--end

local Players = game:GetService("Players")

local function scoreup(otherPart)
	local character = otherPart.Parent
	local humanoid = character:FindFirstChildWithIsA("Humanoid")
	if humanoid then
		print(humanoid)
	end
	
	local playerList = Players:GetPlayers()
	for i = 1, #playerList do
		local player = playerList[i]
		if player then
			print(player)
		end
	end
end


--while true do
for _, cir in ipairs(eachcircle) do
	cir.Touched:Connect(function(otherPart)
		scoreup(otherPart)
	end)
end
--end
platenocode.txt
2 KB