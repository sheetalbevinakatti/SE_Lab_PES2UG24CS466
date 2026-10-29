from thermostat_control import target_temperature, hvac_action, energy_alert


def test_target_temperature_modes_and_times():
    assert target_temperature("away", True, 12) == 16
    assert target_temperature("sleep", True, 23) == 18
    assert target_temperature("sleep", True, 12) == 20
    assert target_temperature("home", False, 12) == 18
    assert target_temperature("home", True, 7) == 22
    assert target_temperature("home", True, 18) == 21
    assert target_temperature("home", True, 12) == 20


def test_hvac_action_paths():
    assert hvac_action(20, 20.5, 10) == "idle"
    assert hvac_action(18, 20, 10) == "heat"
    assert hvac_action(22, 20, 35) == "cool_boost"
    assert hvac_action(22, 20, 20) == "cool"


def test_energy_alert_paths():
    assert energy_alert([], 10) == "ok"
    assert energy_alert([8, 10], 10) == "ok"
    assert energy_alert([11, 10], 10) == "warning"
    assert energy_alert([11, 12, 10], 10) == "critical"
