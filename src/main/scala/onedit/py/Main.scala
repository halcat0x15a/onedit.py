package onedit.py

import java.io.InputStreamReader

import javax.script._

object Main extends App {
  val engine = (new ScriptEngineManager).getEngineByName("python")
  engine.eval(new InputStreamReader(getClass.getResourceAsStream("/main.py")))
}
