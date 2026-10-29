from thermostat_control import target_temperature, hvac_action, energy_alert


def test_target_temperature_branches():
    assert target_temperature("away", True, 12) == 16
    assert target_temperature("sleep", True, 5) == 18
    assert target_temperature("sleep", True, 6) == 20
    assert target_temperature("sleep", True, 22) == 18
    assert target_temperature("home", False, 12) == 18
    assert target_temperature("home", True, 6) == 22
    assert target_temperature("home", True, 9) == 20
    assert target_temperature("home", True, 17) == 21
    assert target_temperature("home", True, 22) == 20


def test_hvac_action_branches():
    assert hvac_action(20, 20.5, 10) == "idle"
    assert hvac_action(18, 20, 4) == "heat_boost"
    assert hvac_action(18, 20, 5) == "heat"
    assert hvac_action(22, 20, 31) == "cool_boost"
    assert hvac_action(22, 20, 30) == "cool"


def test_energy_alert_branches():
    assert energy_alert([], 10) == "ok"
    assert energy_alert([8, 10], 10) == "ok"
    assert energy_alert([11, 10], 10) == "warning"
    assert energy_alert([11, 12, 10], 10) == "critical"
