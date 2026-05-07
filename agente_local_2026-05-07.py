#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Projeto de Agente Local - Local Task Planning Agent
Local Agent Project - Simple intelligent task planning system

This is a simple autonomous agent that helps plan and prioritize tasks
using a priority scoring algorithm and task analysis.

Author: Jonathan Ferreira Soares
Date: 2026-05-07
"""

from datetime import datetime
import json

class TaskAgent:
      """
          Agente Local para Planejamento de Tarefas
              Local Agent for Task Planning
                  """

    def __init__(self):
              self.tasks = []
              self.completed = []

    def add_task(self, description: str, priority: int = 1, due_date: str = None):
              """
                      Adiciona uma nova tarefa ao agente
                              Add a new task to the agent
                                      """
              task = {
                  "id": len(self.tasks) + 1,
                  "description": description,
                  "priority": max(1, min(5, priority)),  # 1-5 scale
                  "due_date": due_date,
                  "created_at": datetime.now().isoformat(),
                  "status": "pending"
              }
              self.tasks.append(task)
              print(f"✓ Tarefa adicionada / Task added: {description}")
              return task["id"]

    def calculate_priority_score(self, task: dict) -> float:
              """
                      Calcula um score de prioridade baseado em múltiplos fatores
                              Calculate priority score based on multiple factors
                                      """
              score = task["priority"] * 10

        # Bonus for tasks with due dates
              if task["due_date"]:
                            try:
                                              due = datetime.fromisoformat(task["due_date"])
                                              days_until = (due - datetime.now()).days
                                              if days_until <= 1:
                                                                    score += 50
              elif days_until <= 3:
                                    score += 30
elif days_until <= 7:
                    score += 15
            except:
                pass

        return score

    def prioritize_tasks(self) -> list:
              """
                      Organiza tarefas por prioridade
                              Organize tasks by priority
                                      """
              if not self.tasks:
                            return []

              sorted_tasks = sorted(
                  self.tasks,
                  key=lambda t: self.calculate_priority_score(t),
                  reverse=True
              )
              return sorted_tasks

    def get_next_task(self) -> dict:
              """
                      Retorna a próxima tarefa mais importante
                              Return the next most important task
                                      """
              pending = [t for t in self.tasks if t["status"] == "pending"]
              if not pending:
                            return None

              prioritized = sorted(
                  pending,
                  key=lambda t: self.calculate_priority_score(t),
                  reverse=True
              )
              return prioritized[0] if prioritized else None

    def complete_task(self, task_id: int) -> bool:
              """
                      Marca uma tarefa como concluída
                              Mark a task as completed
                                      """
              for task in self.tasks:
                            if task["id"] == task_id:
                                              task["status"] = "completed"
                                              task["completed_at"] = datetime.now().isoformat()
                                              self.completed.append(task)
                                              print(f"✓ Tarefa concluída / Task completed: {task['description']}")
                                              return True
                                      return False

    def show_agenda(self):
              """
                      Exibe a agenda de tarefas organizadas
                              Display the organized task agenda
                                      """
              print("\n" + "="*60)
              print("AGENDA DO AGENTE / AGENT'S SCHEDULE")
              print("="*60)

        prioritized = self.prioritize_tasks()
        if not prioritized:
                      print("Nenhuma tarefa / No tasks")
                      return

        for i, task in enumerate(prioritized, 1):
                      status = "✓" if task["status"] == "completed" else "○"
                      print(f"\n{i}. [{status}] {task['description']}")
                      print(f"   Prioridade / Priority: {task['priority']}/5")
                      if task['due_date']:
                                        print(f"   Data de vencimento / Due: {task['due_date']}")
                                    print(f"   Score: {self.calculate_priority_score(task):.1f}")


def main():
      """
          Demonstração do Agente Local
              Local Agent Demonstration
                  """
    agent = TaskAgent()

    # Exemplos de tarefas / Task examples
    agent.add_task("Estudar Python", priority=4)
    agent.add_task("Fazer exercício", priority=3, due_date="2026-05-08")
    agent.add_task("Ler documentação", priority=5, due_date="2026-05-07")
    agent.add_task("Organizar arquivos", priority=2)
    agent.add_task("Revisar código", priority=4, due_date="2026-05-09")

    # Mostra agenda priorizada
    agent.show_agenda()

    # Simula conclusão de tarefas
    next_task = agent.get_next_task()
    if next_task:
              print(f"\nProxima tarefa / Next task: {next_task['description']}")
              agent.complete_task(next_task["id"])

    print("\n" + "="*60)
    print(f"Total de tarefas / Total tasks: {len(agent.tasks)}")
    print(f"Concluídas / Completed: {len(agent.completed)}")
    print("="*60)


if __name__ == "__main__":
      main()
