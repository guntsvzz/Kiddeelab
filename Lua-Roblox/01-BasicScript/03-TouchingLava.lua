local lava = script.Parent

local function kill(otherPart)
    local partParent = otherPart.Parent
    -- The Humanoid, a special object which contains many properties related to the user, 
    -- including the user's health
    local humanoid = partParent:FindFirstChild("Humanoid")
    -- FindFirstChild function - just pass it the name of the thing you're looking for 
    -- and it will provide the first matching child it finds in that object
    if humanoid then
        humanoid.Health = 0
    end
end

lava.Touched:Connect(kill)