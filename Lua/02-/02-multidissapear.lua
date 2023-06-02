local box1 = game.Workspace.Box1
local box2 = game.Workspace.Box2
local box3 = game.Workspace.Box3

local function disappear(box)
	box.CanCollide = false
	box.Transparency = 1
end

local function appear(box)
	box.CanCollide = true
	box.Transparency = 0
end

local isTouched = false
local function fade(box)
	if not isTouched then
		isTouched = true
		for count = 1, 10 do
			box.Transparency = count / 10
			wait(0.1)
		end
		box.CanCollide = false
		wait(3)
		box.CanCollide = true
		box.Transparency = 0
		isTouched = false
	end
end

while true do
	wait(1)
	disappear(box1)
	wait(1)
	appear(box1)
	wait(1)
	disappear(box2)
	wait(1)
	appear(box2)
	wait(1)
	disappear(box3)
	wait(1)
	appear(box3)
end


--local Players = game:GetService("Players")

--local function onCharacterAdded(character, player)
--	player:SetAttribute("IsAlive", true)
--	local humanoid = character:WaitForChild("Humanoid")
--	humanoid.Died:Connect(function()
--		local points = player.leaderstats.Points
--		points.Value = 0
--		player:SetAttribute("IsAlive", false)
--	end)
--end

--local function onPlayerAdded(player)
--	local leaderstats = Instance.new("Folder")
--	leaderstats.Name = "leaderstats"
--	leaderstats.Parent = player

--	local points = Instance.new("IntValue")
--	points.Name = "Points"
--	points.Value = 0
--	points.Parent = leaderstats

--	player:SetAttribute("IsAlive", false)

--	player.CharacterAdded:Connect(function(character)
--		onCharacterAdded(character, player)
--	end)
--end

--Players.PlayerAdded:Connect(onPlayerAdded)

--while true do
--	wait(1)
--	local playerList = Players:GetPlayers()
--	for i = 1, #playerList  do
--		local player = playerList[i]
--		if player:GetAttribute("IsAlive") then
--			local points = player.leaderstats.Points
--			points.Value = points.Value + 1
--		end
--	end
--end