package de.geroldbusch.helloworld;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class EnvironmentController {
    @GetMapping("/stage")
    public String getEnv() {
        return System.getenv("stage");
    }
}
