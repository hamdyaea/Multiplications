#!/usr/bin/env python3
# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-or-later
"""Interactive multiplication practice with a Tkinter desktop interface."""
from __future__ import annotations

import argparse
import secrets
from pathlib import Path
import tkinter as tk
from tkinter import messagebox


def question() -> tuple[int, int]:
    return secrets.randbelow(10) + 2, secrets.randbelow(10) + 2


def grade(correct: int, total: int) -> float:
    if total <= 0 or not 0 <= correct <= total:
        raise ValueError("Invalid score")
    return round(1 + 5 * correct / total, 2)


class MultiplicationApp(tk.Tk):
    QUESTIONS = 20

    def __init__(self) -> None:
        super().__init__()
        self.title("Multiplication Trainer · Hamdy Abou El Anein")
        self.happy = tk.PhotoImage(file=str(Path(__file__).resolve().parent / "Pictures/happy-ui.png"))
        self.sad = tk.PhotoImage(file=str(Path(__file__).resolve().parent / "Pictures/sad-ui.png"))
        self.minsize(410, 350)
        self.configure(bg="#101827")
        self.correct = 0
        self.index = 0
        self.current = (2, 2)
        self.progress = tk.StringVar()
        self.prompt = tk.StringVar()
        self.feedback = tk.StringVar()
        self.answer = tk.StringVar()
        panel = tk.Frame(self, bg="#101827", padx=30, pady=24)
        panel.pack(expand=True, fill="both")
        tk.Label(panel, text="MULTIPLICATION TRAINER", font=("DejaVu Sans", 13, "bold"),
                 bg="#101827", fg="#8bd6c1").pack(pady=(0, 20))
        tk.Label(panel, textvariable=self.progress, font=("DejaVu Sans", 11),
                 bg="#101827", fg="#c7d4e4").pack()
        tk.Label(panel, textvariable=self.prompt, font=("DejaVu Sans", 34, "bold"),
                 bg="#101827", fg="#f2c879").pack(pady=(20, 12))
        self.entry = tk.Entry(panel, textvariable=self.answer, font=("DejaVu Sans", 20),
                              justify="center", width=10)
        self.entry.pack()
        self.picture = tk.Label(panel, bg="#101827")
        self.picture.pack()
        tk.Label(panel, textvariable=self.feedback, font=("DejaVu Sans", 11),
                 bg="#101827", fg="#c7d4e4", wraplength=400).pack(pady=12)
        self.submit = tk.Button(panel, text="Check answer", command=self.check,
                                bg="#7ddcc0", fg="#10211c", font=("DejaVu Sans", 11, "bold"),
                                relief="flat", padx=18, pady=9)
        self.submit.pack()
        tk.Button(panel, text="Start again", command=self.reset,
                  bg="#293a50", fg="#ffffff", relief="flat", padx=12, pady=7).pack(pady=12)
        self.bind("<Return>", lambda _event: self.check())
        self.reset()

    def reset(self) -> None:
        self.index = self.correct = 0
        self.submit.config(state="normal")
        self.feedback.set("")
        self.picture.configure(image="")
        self.next_question()

    def next_question(self) -> None:
        self.current = question()
        self.progress.set(f"Question {self.index + 1} / {self.QUESTIONS} · {self.correct} correct")
        self.prompt.set(f"{self.current[0]} × {self.current[1]} = ?")
        self.answer.set("")
        self.entry.focus_set()

    def check(self) -> None:
        if self.index >= self.QUESTIONS:
            return
        try:
            response = int(self.answer.get().strip())
        except ValueError:
            self.feedback.set("Please enter a whole number.")
            return
        expected = self.current[0] * self.current[1]
        self.picture.configure(image=self.happy if response == expected else self.sad)
        self.correct += response == expected
        self.index += 1
        self.feedback.set("Correct!" if response == expected else f"Answer: {expected}")
        if self.index == self.QUESTIONS:
            self.submit.config(state="disabled")
            self.progress.set(f"Completed · {self.correct}/{self.QUESTIONS} correct")
            self.prompt.set(f"Grade: {grade(self.correct, self.QUESTIONS):.2f} / 6")
            self.answer.set("")
        else:
            self.next_question()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--grade", nargs=2, type=int, metavar=("CORRECT", "TOTAL"),
                        help="Calculate the Swiss 1–6 grade in the terminal")
    args = parser.parse_args()
    if args.grade is not None:
        print(grade(*args.grade))
    else:
        MultiplicationApp().mainloop()


if __name__ == "__main__":
    main()
