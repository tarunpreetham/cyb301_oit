rule CYB301_Benign_simulator
{
	strings:
		$a = "CYB301_TEST.txt"
		$b = "CYB301 benign simulator"

	condition:
		all of them
}
