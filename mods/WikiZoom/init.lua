-- WikiZoom: set the gameplay camera distance from config 'distance', live.
-- Proven in game 2026-10-15. Shipped Hero_Common cameras: distance 33
-- (Default, Ultimate), 9.05 (Zoom).

local R = require "rsmm"
R.health.checkpoint("per_mod:WikiZoom")

local function say(msg) R.log("[WikiZoom] " .. msg) end

local MIN_OK, MAX_OK = 5, 300     -- a value outside this is not a distance
local MAX_SET = 150
local described, last = false, nil

local function note(msg)          -- one line per change of status, not per poll
    if msg ~= last then last = msg; say(msg) end
end

local function apply()
    if not R.camera then note("R.camera is missing from this SDK build"); return end
    local want = tonumber(R.config.get("distance", 0)) or 0
    if want <= 0 then
        if R.camera.reset() > 0 then note("distance 0: cameras put back") end
        return
    end
    if want > MAX_SET then want = MAX_SET end

    local cur, why = R.camera.get("distance")
    if not cur then note("waiting for the hero camera: " .. tostring(why)); return end
    if not described then described = true; R.camera.describe() end  -- values before any write
    if cur < MIN_OK or cur > MAX_OK then
        note(string.format("REFUSED: the 'distance' record reads %.3f, not a distance (normal is 33); "
            .. "the field mapping is wrong, nothing written. See the [rsmm.camera] lines above.", cur))
        return
    end
    if math.abs(cur - want) < 0.01 then note(string.format("distance already %.2f", cur)); return end
    local n, err = R.camera.set("distance", want, { all = R.config.get("all_cameras", true) and true or false })
    if n then
        note(string.format("distance %.2f -> %.2f on %d camera(s)", cur, want, n))
    else
        note("not written: " .. tostring(err))
    end
end

R.config.on_change("distance", apply)
R.config.on_change("all_cameras", apply)
-- A new hero (next chapter, respawn) gets fresh settings at the patched values.
R.schedule.every(2.0, apply)

R.on("ready", function() say("loaded; set distance in config.toml (0 = off)") end)
